module.exports = {
  extends: ['@alife/eslint-config-sail'],
  overrides: [
    {
      extends: ['plugin:svelte/recommended'],
      files: ['*.svelte'],
      parser: 'svelte-eslint-parser',
      parserOptions: {
        parser: '@typescript-eslint/parser',
      },
      rules: {
        'svelte/no-at-html-tags': 'off',
      },
    },
  ],
  rules: {
    '@typescript-eslint/no-empty-interface': 'off',
  },
};
