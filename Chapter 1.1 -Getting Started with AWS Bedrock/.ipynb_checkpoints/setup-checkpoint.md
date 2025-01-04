### Setting Up a Python Virtual Environment and Using it in Jupyter Notebook

#### **Step 1: Create a Virtual Environment**
Run the following command in your terminal to create a new virtual environment:
```bash
python -m venv bedrock101_env
```

#### **Step 2: Activate the Virtual Environment**
For Linux/macOS, activate the virtual environment using:
```bash
source bedrock101_env/bin/activate
```
For Windows, use:
```cmd
bedrock101_env\Scripts\activate
```

Once activated, your terminal prompt will show the environment name, e.g., `(bedrock101_env)`.

#### **Step 3: Install Necessary Packages**
Install `ipykernel` and any other required libraries in the virtual environment:
```bash
pip install ipykernel
```

#### **Step 4: Add Virtual Environment to Jupyter**
Register the virtual environment as a Jupyter kernel:
```bash
python -m ipykernel install --user --name=bedrock101_env --display-name "Python (bedrock101_env)"
```
This will make the virtual environment available as an option in Jupyter Notebook.

#### **Step 5: Install Additional Dependencies**
Install additional dependencies required for your project. For example:
```bash
pip install langchain==0.1.13 langchain-aws==0.2.10 grpcio==1.68.1 grpcio-tools==1.68.1
```

#### **Step 6: Launch Jupyter Notebook**
Start Jupyter Notebook by running:
```bash
jupyter notebook
```

#### **Step 7: Select the Virtual Environment in Jupyter**
1. Open a notebook.
2. Go to the `Kernel` menu.
3. Select `Change Kernel`.
4. Choose `Python (bedrock101_env)`.

#### **Step 8: Verify the Setup**
Test the setup by importing your desired modules. For example:
```python
from langchain_aws.chat_models import ChatBedrock
print("LangChain AWS successfully imported!")
```

#### **Common Issues and Troubleshooting**
- **Kernel Not Showing in Jupyter:** Ensure `ipykernel` is installed and the environment was correctly registered.
- **Package Conflicts:** Resolve dependency conflicts by installing compatible versions or using the `--force-reinstall` flag.
- **Activate Environment Before Running Commands:** Always activate the environment before installing packages or running scripts.

---
Following these steps ensures a clean setup of your Python virtual environment, ready for use in Jupyter Notebook.

