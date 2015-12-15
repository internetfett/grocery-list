import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('checklist-ingredient', 'Integration | Component | checklist ingredient', {
  integration: true
});

test('it renders', function(assert) {
  
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });" + EOL + EOL +

  this.render(hbs`{{checklist-ingredient}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:" + EOL +
  this.render(hbs`
    {{#checklist-ingredient}}
      template block text
    {{/checklist-ingredient}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
