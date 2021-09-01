import os

def cdEvaluator(path):
    try:
        os.chdir(os.path.abspath(path))
        return True
    except Exception as e:
        return f"Error obtained: {e}"