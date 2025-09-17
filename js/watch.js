async function loadfiles(){
    try{
        const socket = io("http://127.0.0.1:5000");
        socket.on("connect", ()=>{
            console.log("Connected to server via Socket.IO")
        });

        socket.on("server_message",(data) => {
            console.log("Message from server", data.msg);
        });
        
        const res = await fetch("http://127.0.0.1:5000/play-movie")
            .then(data=>{
                document.getElementById("text").textContent = "now watching" + data.folder;
            });
    }catch(err){
        console.error("Error fetching data files: ", err);
    }
}

window.addEventListener("DOMContentLoaded", loadfiles);
