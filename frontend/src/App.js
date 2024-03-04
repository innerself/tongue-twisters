import React, {useEffect, useState} from 'react';
import {Box} from "@mui/system";
import {Button, Typography} from "@mui/material";
import {createTheme, ThemeProvider} from '@mui/material/styles';


const colors = {
    primary: {main: '#5A7582'},
    background: {default: '#EFEBE9'},
    text: {primary: '#272827'},
}


const theme = createTheme({
    palette: {
        primary: colors.primary,
        background: colors.background,
        text: colors.text,
    }
})


function App() {
    const [message, setMessage] = useState('No twisters :(');
    const [twisters, setTwisters] = useState(['asd', 'qwe'])

    useEffect(() => {
        fetch('/api/twisters')
            .then(response => response.json())  // Parse the response as JSON
            .then(dataList => {
                if (dataList && dataList.length > 0) {
                    console.log('Returned data: ', dataList);
                    setTwisters(dataList.slice(0, 5) || ['No twisters in DB :(']);
                    setMessage(dataList[0].text || 'No twisters in DB :(');
                } else {
                    console.error('Empty or invalid data received from the API');
                    // Set a default message or handle the case when data is empty
                    setMessage("Default Message");
                }
            })
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <ThemeProvider theme={theme}>
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    minHeight: '100vh',
                    backgroundColor: theme.palette.background.default,
                }}
            >
                <Box sx={{padding: 5, backgroundColor: theme.palette.primary.main, borderBottom: '1px solid #303F46'}}>
                    <Box sx={{display: 'flex'}}>

                    </Box>
                </Box>

                <Box sx={{
                    flex: 1, display: 'flex', flexDirection: 'column',
                    alignItems: 'center', justifyContent: 'center'
                }}>
                    {twisters.map((item, index) => (
                        <Typography key={index} paragraph={true} variant="h4"
                        gutterBottom={true}>{item.text}</Typography>
                    ))}
                </Box>
                <Button variant='outlined'
                        sx={{ml: "auto", mr: "auto", width: "30%", mb: "5rem", borderColor: '#fc9e81', color: theme.palette.text.primary}}>ДАЛЬШЕ</Button>
                <Box sx={{
                    padding: 5,
                    backgroundColor: theme.palette.primary.main,
                    borderTop: '2px solid #303F46'
                }}></Box>

            </Box>
        </ThemeProvider>
    );
}

export default App;
