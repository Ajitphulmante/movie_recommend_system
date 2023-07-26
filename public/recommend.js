console.log("in recommend.js file");

const fastapi = 'http://localhost:8000/recommed';




const inputData={
    movie_name : String
}

document.getElementById('myform').addEventListener('submit',function(event){
    event.preventDefault();

    const movie = document.getElementById("movie").value;
    console.log("movies name :",movie)
    inputData.movie_name=movie;

    axios.post(fastapi,inputData).then((response)=>{
        const prediction = response.data;
        console.log(prediction);   
        
        console.log(typeof(prediction));

        const arr = prediction['prediction'];

        console.log("arr:",arr);

        console.log(typeof(prediction));

        var ul = document.getElementById('mlist');



        for (var i=0; i<arr.length; i++){

            var li = document.createElement("li");
            ul.appendChild(li);
            li.innerHTML=arr[i];

            
        }
        var li = document.createElement("li");
        for (var i=0; i<arr.length; i++) ul.removeChild('li');

        console.log("for loop ended");
         
    }).catch((err)=>{
         console.log(err);
    })

})
