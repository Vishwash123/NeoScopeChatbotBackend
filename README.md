## Setup Instructions
   
Follow these steps to get the project running locally.

# Step 1:  Clone the Repository and Create a Virtual Environment

Open your terminal or command prompt and navigate to the directory where you want to set up the project.

Create a virtual environment to manage dependencies:

python3 -m venv venv

Activate the virtual environment:

On macOS and Linux:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate

# Step 2: Install Required Libraries

Make sure your virtual environment is active. You should see (venv) at the start of your terminal prompt.

Install all the necessary Python libraries from the requirements.txt file:

pip install -r requirements.txt

# Step 3: Clone and Build llama.cpp

This project uses llama.cpp to run the language model. You need to clone its repository and compile the binaries.

From your project's main directory, clone the llama.cpp repository:

git clone https://github.com/ggerganov/llama.cpp.git

Navigate into the llama.cpp directory:

cd llama.cpp

Compile the source code:

make

Navigate back to your project's main directory:

cd ..

#Step 1.4: Download the LLM Model

You need to download the specific language model file (.gguf) used by the backend.

Go to the Hugging Face model page: [HuggingFaceModelPage](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

Download the mistral-7b-instruct-v0.1.Q4_K_M.gguf file.

In your project's main directory, create a new folder named models.

Move the downloaded model file into the models folder.

Your project structure should now look something like this:

/your-project/

├── chatbot_module.py

├── classify_module.py

├── ...

├── requirements.txt

├── unified_server.py

├── venv/

├── llama.cpp/

└── models/mistral-7b-instruct-v0.1.Q4_K_M.gguf
    
## 2. Running the Backend Server
Once all the setup steps are complete, you can start the backend server.

Ensure your virtual environment is active.

From your project's main directory, run the server file:

python3 unified_server.py

The server should now be running and ready to accept requests.
