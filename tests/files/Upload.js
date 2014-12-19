
/**
 * class for the upload module
 *
 * @TODO use multiupload seen here
 * 
 *
 * @TODO Upload media entity together with picture
 * 
 * http://ext4all.com/post/extjs-4-2-2-html-5-multi-file-upload.html
 * 
 */

// some on  line comment

Ext.define('Lier.media.view.Upload', {
    
    requires: ['Utils.form.MultiFile'],

    extend: 'Ext.form.Panel',

    constructor: function(config) {
        this.initConfig(config);
        this.callParent(arguments);
    },

    title: 'Upload a Photo',
    bodyPadding: 10,
    items: [{
        name: 'image',
        xtype: 'filefield',
        labelWidth: 80,
        fieldLabel: 'Choose file(s)',
        anchor: '100%',
        allowBlank: false,
        margin: 0
    }],

    buttons: [{
        text: 'Upload',
        handler: function() {
            var form = this.up('form').getForm();
            if(form.isValid()){
                form.submit({
                    url: '/survivor/media/upload',
                    waitMsg: 'Uploading your photo...',
                    params: {
                        meta: {some: "encoded json"}
                    },
                    success: function(fp, o) {
                        Ext.Msg.alert('Success', 'Your photo "' + o.result.file + '" has been uploaded.');
                    }
                });
            }
        }
    }]
});