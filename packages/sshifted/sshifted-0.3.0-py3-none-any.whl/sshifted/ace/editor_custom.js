var editor = ace.edit("editor");
function initializeEditor(editorId) {

    editor.setTheme("ace/theme/textmate");
    editor.session.setMode("ace/mode/python");

    // Handle paste command
    editor.commands.addCommand({
        name: 'pasteCommand',
        bindKey: {win: 'Ctrl-V', mac: 'Command-V'},
        exec: function(editor) {
            handler.requestPaste();
            console.log("Paste requested via Ctrl-V in editor " + editorId);
        },
        readOnly: true
    });

    // Handle save command
    editor.commands.addCommand({
        name: "save",
        bindKey: { win: "Ctrl-S", mac: "Command-S" },
        exec: function(editor) {
            handler.saveFromJs();
            console.log("Save requested via Ctrl-S in editor " + editorId);
        }
    });

    // Change detection
    var contentChanged = false;
    var ignoreFirstChange = true;
    editor.getSession().on('change', function() {

        if (ignoreFirstChange) {
            ignoreFirstChange = false;
            return;
        }
        contentChanged = true;
        console.log("Content changed in editor " + editorId);
        handler.contentChanged(editorId);
    });

    // Functions to handle content change tracking
    window['resetContentChanged' + editorId] = function() {
        contentChanged = false;
    };

    window['hasContentChanged' + editorId] = function() {
        return contentChanged;
    };

    return editor; // Return the editor instance if needed
}

function replaceSelectionWithDecodedBase64(base64String) {
    // This function assumes it's being called for the currently active editor
    var editor = ace.edit("editor");
    var decodedString = atob(base64String);
    editor.session.replace(editor.selection.getRange(), decodedString);
}

function resetContentChangedFlag(editorId) {
    if (window["editor" + editorId]) {
        window["editor" + editorId].contentChanged = false;
    }
}

function changeEditorTheme(themeName) {
//alert("got here");
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/" + themeName);
}



