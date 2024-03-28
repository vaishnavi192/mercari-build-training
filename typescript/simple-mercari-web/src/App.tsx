import { useState } from 'react';
import './App.css';
import { ItemList } from './components/ItemList';
import { Listing } from './components/Listing';

function App() {
  // reload ItemList after Listing complete
  const [reload, setReload] = useState(true);
  return (
    <body>
      <header className='Title'>
        <p>
<<<<<<< HEAD
          <b>My First Webpage</b>
=======
          <b>MY FIRST WEBPAGE</b>
>>>>>>> bbeebe98aaf4771a6179d8c707405d756346b894
        </p>
      </header>
      <div>
        <Listing onListingCompleted={() => setReload(true)} />
      </div>
      <div>
        <ItemList reload={reload} onLoadCompleted={() => setReload(false)} />
      </div>
    </body>
  )
}

export default App;