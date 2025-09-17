async function loadfiles(){
    try{

        const socket = io("http://127.0.0.1:5000");
        socket.on("connect", ()=>{
            console.log("Connected to server via Socket.IO")
        });

        socket.on("server_message",(data) => {
            console.log("Message from server", data.msg);
        });


        let count = 0;
        const res = await fetch("http://127.0.0.1:5000/api/videos");
        const data = await res.json();

        const list = document.getElementById("mainmenu");
        const main_div = document.getElementById("container");

        main_div.style.display = "none";

        data.files.forEach(file => {
            count++;
            const containt_movies =  main_div.cloneNode(true);
            containt_movies.style.display = "block";
            containt_movies.classList.add("movie-item");
            containt_movies.setAttribute("data-file",file);
            const text = containt_movies.querySelector("span");
            text.textContent = file;
            list.append(containt_movies)
        });

        document.addEventListener("click", async function(e){
            if(e.target.closest(".movie-item")){
                const movieDiv = e.target.closest(".movie-item");
                const file = movieDiv.getAttribute("data-file");
                

                const res_ser = await fetch("http://127.0.0.1:5000/watch-movie", {
                    method:"POST",
                    headers:{"Content-Type":"application/json"},
                    body: JSON.stringify({folder:file})
                });

                const data2 = await res_ser.json();

                if (data2.status === "success"){
                        alert("clicked: " + file);
                    
                }
                else{
                    alert("wronggggg!")
                }

            }
        });
    }catch(err){
        console.error("Error fetching data files: ", err);
    }
}

window.addEventListener("DOMContentLoaded", loadfiles);