const searchField = document.querySelector("#ck2");
const searchresult = document.querySelector(".searchresult");
const result = document.querySelector(".result");
searchresult.style.display='none';

searchField.addEventListener("keyup",(e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0){
        console.log("searchValue",searchValue);

        fetch("/searchcuisinerestau",{
            body:JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data",data);
            result.style.display='none';
            searchresult.style.display = 'block';
            if (data.length===0){
                searchresult.innerHTML='No results Found'
            }



        });
    }
});