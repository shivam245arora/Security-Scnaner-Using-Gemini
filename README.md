<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# AI Security Scanner for Python

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-security-audit-copy)

**Author:** Shivam Arora  
**Email:** arorashivam419@gmail.com

---

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_tz9xp5km)

---

## Introducing Today's Project!

This project aims to build a simple Python-based security scanner using the Gemini API. The scanner helps developers identify security vulnerabilities in Python code automatically instead of checking the code manually. The user provides a Python file to the scanner, which reads the code and sends it to Gemini AI for analysis. Gemini examines the code and detects common security issues such as SQL injection, hardcoded secrets (passwords or API keys), and weak cryptographic practices. After analyzing the code, Gemini returns a report describing the vulnerabilities and possible improvements. The scanner then displays the results in a clear and readable format in the command line. This project demonstrates how artificial intelligence can be used to improve software security and save development time.

### Key tools and concepts

The key tools I used include in this is Gemini API,Python,Coloroma Librabries. Key concepts I learnt include prompt structuring, code basics and terminal commands.

### Challenges and wins

Today, I completed this project to learn how to integrate the Gemini API key into an application and use it for AI-powered security analysis. I also learned about different types of security vulnerabilities and how a security scanner can identify them. Through this project, I gained hands-on experience with API integration, environment variables, and vulnerability detection. Moving forward, I would like to learn how to implement more advanced features, support additional programming languages, improve vulnerability detection accuracy, and make the scanner more generalized and scalable for real-world use cases. This project helped me strengthen my understanding of both AI integration and cybersecurity concepts.

---

## Generating the Gemini API Key

In this step, we generate a Gemini API Key from Google. The API key is a unique credential that enables our Python security scanner to communicate with the Gemini AI service. Since the scanner depends on Gemini to analyze Python code and detect security vulnerabilities, obtaining the API key is essential. Once generated, the key will be added to our application so it can send code to Gemini and receive security analysis results. This is the first setup step for the project and ensures that the scanner has access to Gemini’s AI capabilities to identify potential security issues in code.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_h3ymx6kd)

---

## Setting Up the Python Environment

In this step, we are setting up the Python environment required for building the security scanner. First, we create a new project folder to organize all project files. Next, we install Python, which will be used to write and run the scanner application. Finally, we create a virtual environment to manage project dependencies separately from other Python projects on the system. A virtual environment helps avoid package conflicts and keeps the project organized. Completing these setup tasks ensures that the development environment is ready, allowing us to start coding and integrating the Gemini API into our security scanner.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_rb4kj7mz)

### Installing the required packages

Now that I have my virtual environment set up, I need to install two Python packages (python-dotenv) for securely storing the Gemini API Key, and another package (google-genai), which recognizes the Gemini calls that were written in Python. This is important for my project because these packages enable secure API key management and allow the application to communicate with the Gemini AI model. Installing them ensures that all required dependencies are available, helping the project run smoothly, securely, and without configuration errors during development and testing.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_pw6dq3ck)

---

## Connecting to the Gemini API

In this step, I'm connecting to Gemini!. I'm going to write my first bit of code for my scanner.py script and then test it. This is important because I need to connect to Gemini with my API key.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_yw8dt2jh)

### Securing the API key with a .env file

I got an error! My error was that exposing an API key directly in the source code can lead to security risks and unauthorized access. Having a .env file is important because it stores sensitive information securely outside the code, preventing accidental exposure when sharing code or uploading projects to GitHub. It also protects the API quota and helps follow secure development practices.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_kn3jm8tb)

### Verifying the connection

I verified the connection by running my script. Gemini responded with an answer that the sky is blue because of a very important reason, which confirmed that my API Key connection is working well.

---

## Engineering the Security Prompt

In this step, we are teaching Gemini to act like a cybersecurity expert instead of a normal chatbot. We give it special instructions on how to check computer code for security problems, bugs, and weaknesses. Then, we test it to make sure it understands these instructions and can find security issues correctly.
In simple words, we are training Gemini to become the "security inspector" of our project so it can help find and explain problems in code.


![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_rk9mb7ys)

---

## Building the File Scanner

In this step, I'm adding file scanning so my scanner can read other files I send it. Then I am going to update my Gemini calls to send real code and verify it's ready.  This is important because it's the core of my scanner.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_jt7px3na)

---

## Running the Security Audit

In this step, I'm testing my scanner by creating a sample code file with a security vulnerability and running it through my scanner. I'll start with one vulnerability first because it makes it easier to check whether the scanner is working correctly. Once I confirm that the scanner can detect the first issue, I'll add more vulnerabilities and scan again to see how well it identifies multiple security problems. This helps me verify that my scanner is accurately analyzing code and reporting security risks.

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_ub6ry1wf)

### Analyzing the vulnerability report

My scanner detected the 4 vulnerabilities. The most surprising vulnerability for me was the "f" bomb. This shows that AI can help with security by identifying issues that might be beyond your control or that you don't know about.

---

## Adding Color-Coded Severity Ratings

In this project extension, I'm adding the Coloroma library to my script. This lets the scanner prioritize the vulnerabilities based on the color, so that high critical vulnerabilities are fixed first

![Image](http://learn.nextwork.org/positive_blue_glamorous_sloth/uploads/ai-security-audit-copy_mj7rc2vy)

### How the color system works

I added colour to my responses by using the coloroma library and updating my prompt + my calls to the gemini to include the colours. So that the severity of the error could be defined easily with the help of this.

---

## Wrapping Up

This project took me approximately 1 hour. The most challenging  part was adding the coloroma part ans well as the sys part in the Python script. 

---

---
