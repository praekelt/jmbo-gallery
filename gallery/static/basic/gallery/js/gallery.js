if (typeof $ != 'undefined')
{

$(document).ready(function(){

    // Resize embedded video on detail page to match container size
    // We're introducing knowledge of jmbo-foundry even though the product has
    // no dependency on it. Pragmatism.
    $('div.videoembed-detail, div.foundry-listing div.item-videoembed').each(function(){
        var el = $(this);
        var iframe = $('iframe', el);
        var wo = iframe.width();
        var ho = iframe.height();
        var w = el.width();
        var h = (ho * w * 1.0) / wo;
        iframe.attr('width', w);
        iframe.attr('height', h);
    });

});

}
