import Ember from 'ember';

export default Ember.Component.extend({
    tagName: 'li',
    classNameBindings: ['status:active', 'isEditing:editing'],

    init() {
        this._super(...arguments);
        this.set('status', false);
        this.set('isEditing', false);
    },

    actions: {
        edit() {
            this.set('isEditing', true);
        },

        save(name) {
            this.set('isEditing', false);
            this.model.set('name', name);
            this.model.save();
        },

        remove() {
            this.model.destroyRecord();
        },

        toggleStatus() {
            this.toggleProperty('status');
        }
    },
});
