# Medical ICD Coding Environment (OpenEnv)

This project is a baseline implementation for the OpenEnv hackathon. It provides a simple environment for mapping patient symptoms to ICD-10 codes.

## Environment Overview
- **Name:** MedicalICD-v1
- **Observation:** Text description of symptoms.
- **Action:** ICD-10 code string.

## Tasks
1. **Easy:** Single symptom (Cough -> R05).
2. **Medium:** Multiple symptoms (Fever + Sore Throat -> J02).
3. **Hard:** Ambiguous/Complex symptoms (Butterfly rash -> M32).

## How to Run

### Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run inference:
   ```bash
   python inference.py
   ```

### Using Docker
1. Build the image:
   ```bash
   docker build -t openenv-agent .
   ```
2. Run the container:
   ```bash
   docker run openenv-agent
   ```

## Example Output
```text
[START] task=task_easy env=MedicalICD-v1 model=gpt-3.5-turbo
[STEP] step=1 action=R05 reward=1.00 done=true error=null
[END] success=true steps=1 score=1.00 rewards=1.00
```
