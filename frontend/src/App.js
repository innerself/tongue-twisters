import React, {useState} from 'react';
import styled, {createGlobalStyle} from "styled-components";
import twisters from "./twisters.js";


const GlobalStyle = createGlobalStyle`
    body {
        background-color: #EFEBE9;
    }
`;

const AppContainer = styled.div`
    display: flex;
    justify-items: center;
    border: 2px solid blue;
    width: 99vw;
    height: 99vh;
`;

const TwisterBlock = styled.div`
    text-align: center;
    border: 1px solid black;
    margin: auto;
    width: 70%;
`;


const TwisterRow = styled.div`
    display: grid;
    grid-template-columns: 1fr 200px;
    align-items: center;
`;


const FontChangeButton = ({name, setFSize, sizeChange}) => {
    return <button
        onClick={() => setFSize((currSize) => currSize + sizeChange)}>
        {name}
    </button>
}

const TwisterText = ({twisterText, fSize}) => {
    return <p style={{fontSize: fSize}}>{twisterText}</p>
}

const TwisterControls = ({setFSize}) => {
    return (
        <span>
            <FontChangeButton name="Increase" setFSize={setFSize} sizeChange={+5}/>
            &nbsp;
            <FontChangeButton name="Decrease" setFSize={setFSize} sizeChange={-5}/>
        </span>
    )
}

const Twister = ({twisterText}) => {
    const [fSize, setFSize] = useState(30)
    return (
        <TwisterRow>
            <TwisterText twisterText={twisterText} fSize={fSize}/>
            <TwisterControls setFSize={setFSize}/>
        </TwisterRow>
    )
};


function App() {
    return (
        <>
            <GlobalStyle/>
            <AppContainer>
                <TwisterBlock>
                    {twisters.map(({id, text}) => (
                        <Twister key={`twister-${id}`} twisterText={text}/>
                    ))}
                </TwisterBlock>
            </AppContainer>
        </>
    );
}

export default App;
