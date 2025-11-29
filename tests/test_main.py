import subprocess
import sys
import os

def test_main_output():
    # Get the path to main.py relative to this test file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_path = os.path.join(base_dir, 'main.py')

    result = subprocess.run([sys.executable, main_path], capture_output=True, text=True)

    assert result.returncode == 0, f"main.py exited with error: {result.stderr}"
    assert "commit prueba" in result.stdout.strip(), f"Expected 'commit prueba' in output, got '{result.stdout}'"
    print("test_main_output passed")

if __name__ == "__main__":
    try:
        test_main_output()
        print("All tests passed")
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
