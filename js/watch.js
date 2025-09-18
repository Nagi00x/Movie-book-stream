async function loadfiles(){
    try{
        const socket = io("http://127.0.0.1:5000");
        socket.on("connect", ()=>{
            console.log("Connected to server via Socket.IO")
        });

        socket.on("server_message",(data) => {
            console.log("Message from server", data.msg);
        });
        
        const res = await fetch("http://127.0.0.1:5000/play-movie");
        const data = await res.json();
        const content = data.folder
        
        try{
            const getFiles = await fetch("http://127.0.0.1:5000/getFiles", {
                method:"POST",
                headers:{"Content-Type":"application/json"},
                body: JSON.stringify({file:content})
            });

            const filesUp = await getFiles.json();
            const container = document.getElementById("List");
            const FileName = document.getElementById("filename");

            FileName.style.display = "none";

            let count = 0;

            filesUp.files.forEach(file => {
                count++;
                const content_file = FileName.cloneNode(true);
                content_file.style.display = "block";
                content_file.classList.add("File-name");
                content_file.setAttribute("data-file", file);
                const text = content_file.querySelector("span");
                text.textContent = count;
                container.append(content_file);
            });

            document.addEventListener("click", async function(e){
                if(e.target.closest(".File-name")){
                    const movieDiv = e.target.closest(".File-name");
                    const file = movieDiv.getAttribute("data-file");
                    const movie = document.getElementById("vid");
                    console.log(file)
                    console.log("clicked")
                    movie.src = "http://127.0.0.1:5000/video/"+file;
                    movie.load();
                    movie.play();
                }
            });
        }catch(err){
        console.error("Error fetching data files: ", err);
        }
    }catch(err){
        console.error("Error fetching data files: ", err);
    }
}

window.addEventListener("DOMContentLoaded", loadfiles);
