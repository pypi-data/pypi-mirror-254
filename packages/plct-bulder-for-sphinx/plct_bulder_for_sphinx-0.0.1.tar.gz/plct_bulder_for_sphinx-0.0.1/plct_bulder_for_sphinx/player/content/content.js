var c_API;

document.addEventListener("DOMContentLoaded", function () {
    if(!PetljaRT)
        return;
    c_API = new ContentPage(PetljaRT);
});

document.addEventListener("click", function(e) {
    if (e.target.tagName == "IMG")
    {
        if(e.target.parentNode && e.target.parentNode.tagName =="A")
            e.target.parentNode.setAttribute("target", "_blank");
    }
    if (e.target.tagName == "A")
    {
        if (e.target.getAttribute("href") && e.target.getAttribute("href").startsWith("http"))
            e.target.setAttribute("target", "_blank");
    }
});

function ContentPage(PetljaRT){
    this.isActivityDone = false;
    this.PetljaRT = PetljaRT;
    this.mainDiv = document.getElementsByClassName('body')[0];
    
    document.documentElement.style.overflow = 'hidden';

    this.PetljaRT.registerContent(window.location.href);
    this.PetljaRT.addContentSettingHandler((contentSettings) => {this.setupPage(contentSettings)});
    this.PetljaRT.addFontSizeHandler((zoomFactor) => {this.changeFontSizeWrapper(zoomFactor)});
    // make a more general handler for this
    this.PetljaRT.registerActivityProgress({
        'progressStatus' :true,
        'score' : 1,
        'maxScore' : 1,
        'lectureType' : 'other'
    });

    
    window.addEventListener("load", () =>{
        this.contentHeight = Math.round(this.mainDiv.scrollHeight + 100);
        this.PetljaRT.registerContentHeight(this.contentHeight);

    });

    new ResizeObserver(() => {
        this.contentHeight = Math.round(this.mainDiv.scrollHeight + 100);
        this.PetljaRT.registerContentHeight(this.contentHeight);
    }).observe(this.mainDiv);

}


ContentPage.prototype.changeFontSizeWrapper = function(zoomFactor){
    changeFontSize(document.body, zoomFactor);
}

ContentPage.prototype.setupPage = function(contentSettings){
    this.changeFontSizeWrapper(contentSettings.contentZoomFactor);
}

function changeFontSize(node, zoomFactor) {
    node.childNodes.forEach(child => {
        if(child.nodeType != Node.TEXT_NODE){
            changeFontSize(child, zoomFactor);
            var currentFontSize = parseFloat(window.getComputedStyle(child, null).getPropertyValue("font-size"));
            if (!isNaN(currentFontSize)) {
                child.style.fontSize = (currentFontSize + zoomFactor).toString() + "px";
            }
        }
    });
};