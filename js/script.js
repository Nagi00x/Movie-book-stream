async function loadfiles(){
    try{
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
            containt_movies.id="container-"+count;
            const text = containt_movies.querySelector("span");
            text.textContent = file;
            list.append(containt_movies)
        });
    }catch(err){
        console.error("Error fetching data files: ", err);
    }
}

window.addEventListener("DOMContentLoaded", loadfiles);