import Ember from 'ember';

export default Ember.Controller.extend({
    sortedItems: Ember.computed.sort('model.checklist_items', '_itemSort'),
    _itemSort: ['status:asc', 'name:asc'],
});
