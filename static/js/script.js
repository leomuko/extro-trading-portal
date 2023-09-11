$(document).ready(function() {

    $('#selectAccordion').select2({
        theme: 'bootstrap'
    });
    $('#inputZip').select2({
        theme: 'bootstrap'
    });
    // $('#inputProduct').select2();
    // function listdata(areas) {
    //     console.log(areas);
    //     let count = 0
    //     let content = []
    //     for (let i=0; i < areas.length; i++){
    //         let temp = {id: i, text: areas[i].fields.name}
    //         content.push(temp)
    //     }

    //     $('#inputZip').select2({
    //         data: content,
    //         width: '100%',
    //         templateResult: formatState
    //     });

    //     function formatState(text) {
    //         str="";
    //         str += "<p style='padding: 2px;'>" + text.text + "</p>";
    //         var $state = $(str);
    //         return $state;
    //     }
    // }

    // listdata(areas);
    // console.log(areas)
    // content = []
    // for (let i=0; i < areas.length; i++) {
    //     content.push(areas[i].fields.name);
    // }
    // console.log(content);
    //  $("#inputZip").autocomplete({
    //     source: content,
    //     autoFocus: true
    //  });

    
})
