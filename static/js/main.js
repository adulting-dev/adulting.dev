const swap_map = () => {
    if (document.getElementById("map").style.display === "none") {
        let static_map = document.querySelector("#static_map");
        let map = document.querySelector("#map");
        mapChild = document.getElementById("mapChild");
        mapChild.width = static_map.width;
        mapChild.height = static_map.height;
        map.style.display = "block";
        map.style.display = "none";
    }
};
