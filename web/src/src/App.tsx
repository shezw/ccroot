import { useState } from 'react'
import './App.css'
import '@mantine/core/styles.css';
import { MantineProvider } from '@mantine/core';
import {Navbar} from "./NavBar";
import {Layout} from "./Layout.js";
import {CoreProvider} from "./context/CoreContext";
import {ApiProvider} from "./context/ApiContext";


function App() {
  const [count, setCount] = useState(0)

  return (
    <MantineProvider>
        <ApiProvider>
            <CoreProvider>
                <Layout />
            </CoreProvider>
        </ApiProvider>
    </MantineProvider>
  )
}

export default App
