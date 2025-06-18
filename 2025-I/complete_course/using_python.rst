How to execute a python File (*.py) from the Anaconda Prompt on Windows
=======================================================================

1. **Open Anaconda Prompt**
   - Click the **Windows Start Menu**, search for **Anaconda Prompt**, and open it.
   - If Anaconda is not installed, go to the `cheatsheet <../cheatsheet.rst>`_ to see how to do install it.

2. **Navigate to Your Python File's Folder**
   - Use the `cd` command to navigate through the directories.
     .. code-block:: bash

        cd C:\Users\<Your-Username>\PythonProjects

   - Replace the previous path with your file's folder real location.
   - Use `dir` to list files/folders in the current directory.

3. **Run the python file**
   - Type the following command:
     .. code-block:: bash

        python your_filename.py

   - Substitute `your_filename.py` with the file you want to execute.
   - If the filename has spaces, wrap it in quotes:
     .. code-block:: bash

        python "my script.py"

4. **Troubleshooting Common Issues**
   - **Python not recognized**: Ensure Anaconda is installed correctly. Try `conda list` to verify.
   - **File not found**: Double-check the folder path and filename.
   - **Syntax errors**: Review your Python code for mistakes.
