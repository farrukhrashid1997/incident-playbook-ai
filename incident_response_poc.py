import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os
import json
import re
from typing import List, Dict, Tuple
import logging
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PlaybookGenerator:
    def __init__(self, gemini_api_key: str, data_path: str = "data"):
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel('models/gemini-2.5-pro')
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self.data_path = data_path
        self.dataset = None
        self.embeddings = None
        
        self.load_data()
        self.create_embeddings()
    
    def load_data(self):
        try:
            # Load training and test data
            train_df = pd.read_parquet(f"{self.data_path}/train-00000-of-00001.parquet")
            test_df = pd.read_parquet(f"{self.data_path}/test-00000-of-00001.parquet")
            
            self.dataset = pd.concat([train_df, test_df], ignore_index=True)
            logger.info(f"Loaded dataset with {len(self.dataset)} records")
            logger.info(f"Dataset columns: {self.dataset.columns.tolist()}")
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def extract_attack_type_from_text(self, text: str) -> str:
        attack_patterns = {
            'ransomware': r'ransomware|ransom|encrypt|crypto|locker',
            'phishing': r'phishing|phish|email|social engineering',
            'malware': r'malware|virus|trojan|worm|spyware',
            'ddos': r'ddos|denial of service|dos attack',
            'insider threat': r'insider|employee|privilege|internal',
            'apt': r'apt|advanced persistent|targeted attack',
            'sql injection': r'sql injection|sqli|database attack',
            'xss': r'xss|cross-site|javascript injection',
            'brute force': r'brute force|password attack|credential stuffing',
            'lateral movement': r'lateral movement|privilege escalation|network traversal'
        }
        
        text_lower = text.lower()
        for attack_type, pattern in attack_patterns.items():
            if re.search(pattern, text_lower):
                return attack_type
        
        return 'general security incident'
    
    def create_embeddings(self):
        try:
            # Extract the response text for embedding
            texts = []
            for _, row in self.dataset.iterrows():
                # Assuming the conversation is in a column - adjust based on actual structure
                conversation_text = str(row.iloc[0])  # Adjust column index/name as needed
                
                # Extract the actual response part (after [/INST])
                if '[/INST]' in conversation_text:
                    response_part = conversation_text.split('[/INST]')[1].strip()
                else:
                    response_part = conversation_text
                
                texts.append(response_part)
            
            # Create embeddings
            logger.info("Creating embeddings...")
            self.embeddings = self.embedding_model.encode(texts)
            logger.info(f"Created embeddings with shape: {self.embeddings.shape}")
            
            # Add attack types to dataset
            self.dataset['attack_type'] = [self.extract_attack_type_from_text(text) for text in texts]
            self.dataset['response_text'] = texts
            
        except Exception as e:
            logger.error(f"Error creating embeddings: {str(e)}")
            raise
    
    def find_similar_examples(self, query: str, attack_type: str = None, top_k: int = 3) -> List[Tuple[int, float, str]]:
        query_embedding = self.embedding_model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        if attack_type:
            mask = self.dataset['attack_type'] == attack_type
            filtered_indices = self.dataset[mask].index.tolist()
            
            filtered_similarities = [(i, similarities[i]) for i in filtered_indices]
            filtered_similarities.sort(key=lambda x: x[1], reverse=True)
            
            results = []
            for i, (idx, score) in enumerate(filtered_similarities[:top_k]):
                results.append((idx, score, self.dataset.iloc[idx]['response_text']))
        else:

            top_indices = np.argsort(similarities)[-top_k:][::-1]
            results = [(idx, similarities[idx], self.dataset.iloc[idx]['response_text']) 
                      for idx in top_indices]
        
        return results
    
    def generate_custom_playbook(self, 
                                attack_type: str,
                                industry: str,
                                severity_level: str,
                                affected_systems: List[str],
                                compliance_requirements: List[str],
                                additional_context: str = "") -> str:
        
        query = f"{attack_type} incident response {industry} {severity_level} {' '.join(affected_systems)}"
        similar_examples = self.find_similar_examples(query, attack_type, top_k=2)
        examples_text = ""
        for i, (idx, score, response_text) in enumerate(similar_examples):
            examples_text += f"\n--- Example {i+1} (Similarity: {score:.3f}) ---\n"
            examples_text += response_text[:1000] + "..." if len(response_text) > 1000 else response_text
            examples_text += "\n"
        prompt = f"""
You are a cybersecurity expert specializing in incident response playbook creation. Generate a detailed incident response playbook based on the following parameters and examples.

**INCIDENT PARAMETERS:**
- Attack Type: {attack_type}
- Industry: {industry}
- Severity Level: {severity_level}
- Affected Systems: {', '.join(affected_systems)}
- Compliance Requirements: {', '.join(compliance_requirements)}
- Additional Context: {additional_context}

**SIMILAR EXAMPLES FROM DATABASE:**
{examples_text}

**REQUIREMENTS:**
1. Follow NIST SP 800-61 Rev 2 incident response lifecycle
2. Include all 6 phases: Preparation, Detection & Analysis, Containment, Eradication, Recovery, and Lessons Learned
3. Tailor the playbook specifically for the {industry} industry
4. Address {severity_level} severity level requirements
5. Include compliance considerations for: {', '.join(compliance_requirements)}
6. Provide specific, actionable steps for each phase
7. Include relevant tools, techniques, and procedures
8. Consider the specific systems mentioned: {', '.join(affected_systems)}

**OUTPUT FORMAT:**
Generate a structured playbook with:
- Title and overview
- Each of the 6 NIST phases with detailed steps
- Industry-specific considerations
- Compliance checkpoints
- Communication templates
- Recovery procedures
- Lessons learned framework

Please generate a comprehensive, practical playbook that security teams can immediately implement.
"""

        try:
            response = self.model.generate_content(prompt)
            logger.info("Similar examples used:")
            for i, (idx, score, _) in enumerate(similar_examples):
                logger.info(f"  Example {i+1}: Similarity score {score:.3f}")
            
            return response.text, prompt
            
        except Exception as e:
            logger.error(f"Error generating playbook: {str(e)}")
            return f"Error generating playbook: {str(e)}"
    
    def get_available_attack_types(self) -> List[str]:
        return sorted(self.dataset['attack_type'].unique().tolist())

# Example usage and testing
def main():
    # Configuration - Replace with your actual API key
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Replace with actual API key
    DATA_PATH = "data"  # Adjust path as needed
    
    try:
        generator = PlaybookGenerator(GEMINI_API_KEY, DATA_PATH)
        print("Available attack types in dataset:")
        for attack_type in generator.get_available_attack_types():
            print(f"  - {attack_type}")
        
        # Mock parameters for testing
        test_parameters = {
            "attack_type": "ransomware",
            "industry": "manufacturing",
            "severity_level": "high",
            "affected_systems": ["SCADA systems", "HMI interfaces", "production databases"],
            "compliance_requirements": ["NIST", "IEC 62443", "ISO 27001"],
            "additional_context": "Attack detected on OT network affecting production line controls"
        }
        
        print("\nGenerating playbook with test parameters...")
        print(f"Parameters: {json.dumps(test_parameters, indent=2)}")
        
        # Generate playbook
        playbook, prompt = generator.generate_custom_playbook(**test_parameters)

        
        # Save to file
        with open("generated_playbook.md", "w", encoding="utf-8") as f:
            f.write(f"# Generated Incident Response Playbook\n\n")
            f.write(f"**Parameters Used:**\n")
            f.write(f"```json\n{json.dumps(test_parameters, indent=2)}\n```\n\n")
            f.write(f"**Prompt used:**\n")
            f.write(prompt)
            f.write(playbook)
        
        print(f"\nPlaybook saved to 'generated_playbook.md'")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")

# Interactive function for user input
def interactive_playbook_generator():
    """Interactive function to get user input and generate playbook"""
    
    GEMINI_API_KEY = input("Enter your Gemini API key: ").strip()
    DATA_PATH = input("Enter path to data directory (default: 'data'): ").strip() or "data"
    
    try:
        generator = PlaybookGenerator(GEMINI_API_KEY, DATA_PATH)
        
        print("\nAvailable attack types:")
        attack_types = generator.get_available_attack_types()
        for i, attack_type in enumerate(attack_types, 1):
            print(f"{i}. {attack_type}")
        
        # Get user inputs
        attack_type = input("\nEnter attack type: ").strip()
        industry = input("Enter industry (e.g., healthcare, finance, manufacturing): ").strip()
        severity_level = input("Enter severity level (low/medium/high/critical): ").strip()
        
        affected_systems_input = input("Enter affected systems (comma-separated): ").strip()
        affected_systems = [s.strip() for s in affected_systems_input.split(",") if s.strip()]
        
        compliance_input = input("Enter compliance requirements (comma-separated): ").strip()
        compliance_requirements = [s.strip() for s in compliance_input.split(",") if s.strip()]
        
        additional_context = input("Enter any additional context (optional): ").strip()
        
        # Generate playbook
        print("\nGenerating playbook...")
        playbook = generator.generate_custom_playbook(
            attack_type=attack_type,
            industry=industry,
            severity_level=severity_level,
            affected_systems=affected_systems,
            compliance_requirements=compliance_requirements,
            additional_context=additional_context
        )
        
        print("\n" + "="*80)
        print("GENERATED PLAYBOOK:")
        print("="*80)
        print(playbook)
        
        # Option to save
        save_option = input("\nSave playbook to file? (y/n): ").strip().lower()
        if save_option == 'y':
            filename = input("Enter filename (default: playbook.md): ").strip() or "playbook.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(playbook)
            print(f"Playbook saved to '{filename}'")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print(os.getenv("GEMINI_API_KEY"))
    # Choose execution mode
    mode = input("Choose mode:\n1. Interactive mode\n2. Test mode with mock data\nEnter choice (1 or 2): ").strip()
    
    if mode == "1":
        interactive_playbook_generator()
    else:
        main()