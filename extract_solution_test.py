import os
from extract_solution import extract_solution

llm_response = r'''
{
  "commentary": "The goal is to create a fancy text generator app using Next.js, TypeScript, and ShadCN UI. It will feature a text input field where users can type text, and the text preview will update dynamically based on the selected font style from a series of buttons. The app will have a top navigation bar with the app's logo on the left, and a footer with copyright and information. There will be over 10 font styles as selectable buttons. All elements will be styled using TailwindCSS with clear structure and spacing.",
  "template": "nextjs-developer",
  "title": "Fancy Text Generator",
  "description": "An interactive app that allows users to generate fancy text with real-time preview and font style selection.",
  "additional_dependencies": [
    "shadcn"
  ],
  "has_additional_dependencies": true,
  "install_dependencies_command": "npm install @shadcn/ui",
  "port": 3000,
  "file_path": "pages/index.tsx",
  "code": "import { useState } from 'react';\nimport { Button } from '@shadcn/ui';\n\nconst FontButton = ({ font, onClick }: { font: string, onClick: () => void }) => (\n  <Button className={`btn-${font} text-sm`} onClick={onClick}>\n    {font}\n  </Button>\n);\n\nconst FontSelector = ({ fonts, onFontSelect }: { fonts: string[], onFontSelect: (font: string) => void }) => (\n  <div className='flex space-x-4 overflow-x-auto'>\n    {fonts.map((font, index) => (\n      <FontButton key={index} font={font} onClick={() => onFontSelect(font)} />\n    ))}\n  </div>\n);\n\nconst FancyTextGenerator = () => {\n  const [text, setText] = useState('Hello, type here...');\n  const [font, setFont] = useState('sans');\n\n  const fonts = ['sans', 'serif', 'monospace', 'cursive', 'fantasy', 'arial', 'verdana', 'courier', 'georgia', 'times', 'tahoma', 'lucida'];\n\n  const handleFontSelect = (font: string) => {\n    setFont(font);\n  };\n\n  return (\n    <div className='flex flex-col h-screen'>\n      <header className='nav bg-teal-600 text-white p-4'>\n        <span className='text-xl'>TypeSpark</span>\n      </header>\n      <main className='flex-1 p-4 flex flex-col items-center justify-center space-y-8'>\n        <input\n          id='text-input'\n          type='text'\n          value={text}\n          onChange={(e) => setText(e.target.value)}\n          className='border p-2 rounded-md text-lg w-full max-w-lg'\n          placeholder='Enter your text here...'\n        />\n        <div id='text-preview' className={`text-${font} text-3xl font-medium`}>{text}</div>\n        <FontSelector fonts={fonts} onFontSelect={handleFontSelect} />\n      </main>\n      <footer className='footer bg-gray-800 text-white p-4 text-center'>\n        <p>&copy; 2025 TypeSpark. All rights reserved.</p>\n      </footer>\n    </div>\n  );\n};\n\nexport default FancyTextGenerator;"
}
'''
try:
    response = extract_solution(llm_response=llm_response)

    for file_name, code in response:
        # Ensure the directory exists before writing the file
        dir_path = os.path.dirname(file_name)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(code)

        assert os.path.isfile(file_name), f"File '{file_name}' was not created."
        print(f"File '{file_name}' written successfully.")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
