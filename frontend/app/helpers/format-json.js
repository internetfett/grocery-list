import Ember from 'ember';

export function formatJson(params) {
    let value = params[0];
    return JSON.stringify(value);
}

export default Ember.Helper.helper(formatJson);
