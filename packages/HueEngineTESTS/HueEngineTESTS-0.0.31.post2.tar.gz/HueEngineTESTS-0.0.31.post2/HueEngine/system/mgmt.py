#  Hue Engine ©️
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

from HueEngine.__core__ import tk,filedialog

def newHueScript():
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the file save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python files", "*.py")],
        title="Choose a location and filename"
    )

    # Check if a file path was selected
    if file_path:
        # Define the content of the new file
        content = """import HueEngine

@HueEngine.HueScript(HueEngine.TransformComponent)
class MyScript:
    def __onCall__(self):
        print("My Script OnCall Function!")
        print(self.TransformComponent.x)
    
    def __fixedUpdate__(self):
        print("My Script FixedUpdate Function!")

    def __post__(self):
        print("Optional PostProcessing Logic")
"""

        # Write the content to the file
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File created successfully at {file_path}")
    else:
        print("File creation was cancelled.")
