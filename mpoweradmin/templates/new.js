
let url= https://employeedetails.free.beeceptor.com/my/api/path
    const response = await fetch(url);
    var data = await response.json();
    console.log("Data: ",data)