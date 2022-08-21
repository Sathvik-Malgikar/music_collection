recommended = document.querySelector("#recommended")
item = recommended.dataset.item
name0 = recommended.dataset.name

hoverHandle = ()=>{

    recommended.textContent = "Recommended for you : "+item
    recommended.classList.add("marquee")
    recommended.classList.remove("recommended")
}
leaveHandle = ()=>{
    
    recommended.textContent = "Recommended for you : "+name0
    recommended.classList.add("recommended")
    recommended.classList.remove("marquee")
}
    clickHandle = ()=>{
    window.location.href="/library/getmedia/?it="+item
}

recommended.addEventListener('mouseover',hoverHandle)
recommended.addEventListener('mouseleave',leaveHandle)
recommended.addEventListener('click',clickHandle)