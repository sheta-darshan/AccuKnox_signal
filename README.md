
# AccuKnox Signal Testing

This repository contains code to demonstrate the behavior of Django signals in relation to threading, transaction handling, and execution flow.

## Setup Instructions

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/sheta-darshan/AccuKnox_signal.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`bash
   cd AccuKnox_signal
   \`\`\`

3. Create a virtual environment:
   \`\`\`bash
   python -m venv venv
   \`\`\`

4. Activate the virtual environment:

   - **On Windows**:
     \`\`\`bash
     .\venv\Scripts\activate
     \`\`\`
   - **On macOS/Linux**:
     \`\`\`bash
     source venv/bin/activate
     \`\`\`

5. Install the required dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

6. Apply migrations:
   \`\`\`bash
   python manage.py migrate
   \`\`\`

---

## Testing Answers

### **Testing Answer 1 and 2 (Signal Synchronous and Threading Behavior)**

To test whether Django signals are executed synchronously and run in the same thread as the caller, simply run the following command:

\`\`\`bash
python manage.py test
\`\`\`

This will run the unit tests for **Answer 1** and **Answer 2**.

### **Testing Answer 3 (Signal Transaction Behavior)**

To test whether Django signals run in the same database transaction as the caller, start the Django development server and visit the URL endpoint that triggers the signal:

1. Start the server:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

2. In your browser, visit the following URL:
   \`\`\`
   http://127.0.0.1:8000/create/
   \`\`\`

This will trigger a database transaction and demonstrate the signal's behavior with transactions.

---

## Important Notes

- **Answer 1**: Demonstrates that Django signals are executed synchronously by default.
- **Answer 2**: Confirms that Django signals run in the same thread as the caller.
- **Answer 3**: Shows that Django signals run within the same database transaction as the caller.
- **Answer 4**: see answer.py file in end

---
