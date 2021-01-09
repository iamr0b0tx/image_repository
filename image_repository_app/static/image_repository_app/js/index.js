// the search input field
const searchQuery = document.getElementById("query");

// submits the query typed in the search input
function submitSearchQuery(){
    let query = searchQuery.value.trim();

    if(query.length > 0){
        document.location.href = `${document.location.origin}/search/${query}/`

    }else{
        document.location.href = document.location.origin
    }
}