module.exports = {
  extends: ['@alife/stylelint-config-sail'],
  rules: {
    'selector-class-pattern': null,
  },
  ignoreFiles: ['**/frontend/compiled/build-assets/**', '**/backend/**'],
};
