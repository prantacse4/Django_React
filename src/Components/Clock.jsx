import React, { useState,useEffect } from "react";

const Clock = (props) => {
    const [date, setDate] = useState({
        date: new Date(),
        local: 'bn-BD',
    });

    useEffect(() => {
        setDate({date:new Date(),}) 
    }, [])
   
    function handleClick() {
        console.log("This is clicked");
    }
    return (
        <div>
            <h1>Hello -  { date.date.toLocaleTimeString(date.local) }</h1>
            <button onClick={handleClick}>Click</button>
        </div>
    );
};

export default Clock;
