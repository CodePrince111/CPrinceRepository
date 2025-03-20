import { useState } from 'react';
import { Button } from '@/components/ui/button';

const FontButton = ({ font, onClick }: { font: string, onClick: () => void }) => (
  <Button className={`btn-${font} text-sm`} onClick={onClick}>
    {font}
  </Button>
);

const FontSelector = ({ fonts, onFontSelect }: { fonts: string[], onFontSelect: (font: string) => void }) => (
  <div className='flex space-x-4 overflow-x-auto'>
    {fonts.map((font, index) => (
      <FontButton key={index} font={font} onClick={() => onFontSelect(font)} />
    ))}
  </div>
);

const FancyTextGenerator = () => {
  const [text, setText] = useState('Hello, type here...');
  const [font, setFont] = useState('sans');

  const fonts = ['sans', 'serif', 'monospace', 'cursive', 'fantasy', 'arial', 'verdana', 'courier', 'georgia', 'times', 'tahoma', 'lucida'];

  const handleFontSelect = (font: string) => {
    setFont(font);
  };

  return (
    <div className='flex flex-col h-screen'>
      <header className='nav bg-teal-600 text-white p-4'>
        <span className='text-xl'>TypeSpark</span>
      </header>
      <main className='flex-1 p-4 flex flex-col items-center justify-center space-y-8'>
        <input
          id='text-input'
          type='text'
          value={text}
          onChange={(e) => setText(e.target.value)}
          className='border p-2 rounded-md text-lg w-full max-w-lg'
          placeholder='Enter your text here...'
        />
        <div id='text-preview' className={`text-${font} text-3xl font-medium`}>{text}</div>
        <FontSelector fonts={fonts} onFontSelect={handleFontSelect} />
      </main>
      <footer className='footer bg-gray-800 text-white p-4 text-center'>
        <p>&copy; 2025 TypeSpark. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default FancyTextGenerator;