import Ember from 'ember';

export default Ember.Route.extend({
    //_appContextModelAttrs: ['pageHeader'],
    //_appContextVars: ['pageFooter'],
    //pageHeader: 'name',
    //pageFooter: 'This is the footer content.',
    title: 'Checklist',
    model(params) {
        return this.store.findRecord('checklist', params.id);
    },
});
