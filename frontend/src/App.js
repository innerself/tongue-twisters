import React, {useEffect, useState} from 'react';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('/api/twisters')
            .then(response => response.json())  // Parse the response as JSON
            .then(dataList => {
                if (dataList && dataList.length > 0) {
                    console.log('Returned data: ', dataList);
                    setMessage(dataList[0].text || 'No twisters :(');
                } else {
                    console.error('Empty or invalid data received from the API');
                    // Set a default message or handle the case when data is empty
                    setMessage("Default Message");
                }
            })
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div className="App">
            <h1>{message}</h1>
        </div>
    );
}

export default App;
