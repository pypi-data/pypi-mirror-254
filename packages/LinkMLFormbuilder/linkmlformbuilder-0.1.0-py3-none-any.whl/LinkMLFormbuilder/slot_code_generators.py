from LinkMLFormbuilder import utils
# import utils

def getNumberSlotCode(slotCode, desc, required, propertyName, title):
    rangeDeclaration = ""
    if ("minimum_value" in slotCode and "maximum_value" in slotCode):
      rangeDeclaration = "The value for this field should be between {min} and {max}".format(min = slotCode.get("minimum_value"), max = slotCode.get("maximum_value"))
    elif ("minimum_value" in slotCode):
      rangeDeclaration = "The value for this field should be equal to or greater than {min}".format(min = slotCode.get("minimum_value"))
    elif ("maximum_value" in slotCode):
       rangeDeclaration = "The value for this field should be equal to or smaller than {max}".format(max = slotCode.get("maximum_value"))
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="{propertyName}-addon">{title}</span>
      <input type="number" class="form-control" id="{propertyName}" aria-describedby="{propertyName}-addon {propertyName}-description" {required}>
    </div>
    <div class="form-text" id="{propertyName}-description">{desc} {rangeDeclaration}</div>
  </div>\n'''.format(propertyName = propertyName, required = required, desc = desc, title = title, rangeDeclaration = rangeDeclaration)

def getBooleanSlotCode(desc, required, propertyName, title):
    code = '''<div class="mb-3">
            <div class="input-group">\n'''
    code += '''<span class="input-group-text">{slotName}</span>\n'''.format(slotName = title)
    code += '''<input type="text" class="form-control hidden">\n</div>\n'''
    code += '''<div class="form-text" id="{propertyName}-description">{desc}</div>\n'''.format(propertyName = propertyName, desc = desc)
    code += "<div class='answer-options'>\n"
    code += '''<div class="form-check">
                  <input class="form-check-input" type="radio" name="{enumName}" id="{item}" {required}>
                  <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = propertyName, item = "True", required = required)
    code += '''<div class="form-check">
                  <input class="form-check-input" type="radio" name="{enumName}" id="{item}" {required}>
                  <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = propertyName, item = "False", required = required)
    code += "</div>\n</div>\n"     
    return code

def getEnumSlotCode(slotCode, content, desc, required, propertyName, title):
    multivalued = True if (("multivalued" in slotCode and slotCode.get("multivalued") == True) or ("maximum_cardinality" in slotCode and slotCode.get("maximum_cardinality") > 1)) else False
    
    code = '''<div class="mb-3">
            <div class="input-group">\n'''
    code += '''<span class="input-group-text">{slotName}</span>\n'''.format(slotName = title)
    code += '''<input type="text" class="form-control hidden">\n</div>\n'''
    code += '''<div class="form-text" id="{propertyName}-description">{desc}</div>\n'''.format(propertyName = propertyName, desc = desc)
    for enum in slotCode.get("values_from"):
        if (enum not in content.get("enums")):
           return getTextareaSlotCode(desc, required, propertyName, title)
        enumCode = content.get("enums").get(enum)
        enumName = utils.extractName(enumCode)
        # code += '''<h3>{enumName}</h3>\n'''.format(enumName = enumName)
        code += "<div class='answer-options'>\n<span class='values-from'>" + enumName + ":</span>\n"
        
        for value in enumCode.get("permissible_values"): # TODO: work with enum permissible value slots
            if (not multivalued):
              code += '''<div class="form-check">
                  <input class="form-check-input" type="radio" name="{enumName}" id="{item}" {required}>
                  <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = enumName, item = value, required = required)
            else:
                 code += '''<div class="form-check">
                  <input class="form-check-input" type="checkbox" name="{enumName}" id="{item}" {required}>
                  <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = enumName, item = value, required = required)
        code += "</div>\n"
    code += "</div>\n"        
    return code

def getInlineEnumSlotCode(slotCode, desc, required, propertyName, title):
    multivalued = True if (("multivalued" in slotCode and slotCode.get("multivalued") == True) or ("maximum_cardinality" in slotCode and slotCode.get("maximum_cardinality") > 1)) else False
    if ("permissible_values" not in slotCode):
        return getTextareaSlotCode(desc, required, propertyName, title)

    code = '''<div class="mb-3">
            <div class="input-group">\n'''
    code += '''<span class="input-group-text">{slotName}</span>\n'''.format(slotName = title)
    code += '''<input type="text" class="form-control hidden">\n</div>\n'''
    code += '''<div class="form-text" id="{propertyName}-description">{desc}</div>\n'''.format(propertyName = propertyName, desc = desc)
    enumCode = slotCode.get("enum_range")
    enumName = utils.extractName(enumCode)
    code += "<div class='answer-options'>\n<span class='values-from'>" + enumName + ":</span>\n"
    for value in enumCode.get("permissible_values"):
      if (not multivalued):
        code += '''<div class="form-check">
            <input class="form-check-input" type="radio" name="{enumName}" id="{item}" {required}>
            <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = enumName, item = value, required = required)
      else:
            code += '''<div class="form-check">
            <input class="form-check-input" type="checkbox" name="{enumName}" id="{item}" {required}>
            <label class="form-check-label" for="{item}">{item}</label></div>\n'''.format(enumName = enumName, item = value, required = required)
    code += "</div>\n</div>\n"        
    return code

def getStringSlotCode(desc, required, propertyName, title):
    return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="{propertyName}-addon">{title}</span>
      <input type="text" class="form-control" id="{propertyName}" aria-describedby="{propertyName}-addon {propertyName}-description" {required}>
    </div>
    <div class="form-text" id="{propertyName}-description">{desc}</div>
  </div>\n'''.format(propertyName = propertyName, required = required, desc = desc, title = title)

def getTextareaSlotCode(desc, required, propertyName, title):
   return '''<div class="mb-3">
    <div class="input-group">
      <span class="input-group-text" id="{propertyName}-addon">{title}</span>
      <textarea rows="6" class="form-control" id="{propertyName}" aria-describedby="{propertyName}-addon {propertyName}-description" {required}></textarea>
    </div>
    <div class="form-text" id="{propertyName}-description">{desc}</div>
  </div>\n'''.format(propertyName = propertyName, required = required, desc = desc, title = title)