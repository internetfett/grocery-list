import DS from 'ember-data';

export default DS.Model.extend({
    status: DS.attr(),
    amount: DS.attr(),
    unit: DS.attr(),
    display_amount: DS.attr(),
    name: DS.attr(),
});
