(async () =>  {
    // code....
    console.log("test");
    
    const tally = parseInt(await (await fetch("/tally")).text());
    
    document.getElementById('text1').innerHTML = "You are the " + tally + "th person to be rickrolled here.";
})();