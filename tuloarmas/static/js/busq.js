/*! jQuery v1.10.2 | (c) 2005, 2013 jQuery Foundation, Inc. | jquery.org/license
//@ sourceMappingURL=jquery-1.10.2.min.map
*/
jQuery.fn.filterByText = function(textbox, selectSingleMatch) {
  return this.each(function() {
    var select = this;
    var options = [];
    $(select).find('option').each(function() {
      options.push({value: $(this).val(),id: $(this).attr('id') , text: $(this).text()});
    });
    $(select).data('options', options);
    $(textbox).bind('change keyup', function() {
      var options = $(select).empty().scrollTop(0).data('options');
      var search = $.trim($(this).val());
      var regex = new RegExp(search,'gi');
 
      $.each(options, function(i) {
        var option = options[i];
        if(option.text.match(regex) !== null) {
            var cont = $('select option#'+option.id).length;
            if(cont == 0){
                $(select).append(
                   $('<option>').text(option.text).val(option.value).attr('id',option.id)
                );
            }
        }
      });
      if (selectSingleMatch === true &&
          $(select).children().length === 1) {
        $(select).children().get(0).selected = true;
      }
    });
  });
};
