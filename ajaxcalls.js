// This javascript file contains all ajax related functions required to be used
// to operate the .html appliaction.


    function getAll(callback){
        $.ajax({
            "url": "/myMovies",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }


    function createMovie(movie, callback){
        
        console.log(JSON.stringify(movie));
        $.ajax({
            "url": "/myMovies",
            "method":"POST",
            "data":JSON.stringify(movie),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }   
   
    function updateMovie(movie, callback){
        console.log("updating: " + JSON.stringify(movie));
        $.ajax({
            "url": "/myMovies/"+encodeURI(movie.id),
            "method":"PUT",
            "data":JSON.stringify(movie),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
               console.log(result);
               callback(result)
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    
    function deleteMovie(id, callback){
        
        //console.log(JSON.stringify('deleting '+id));
        $.ajax({
            "url": "/myMovies/"+ id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }