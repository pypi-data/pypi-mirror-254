const prettierConfig = require('@alife/prettier-config-sail')(false);
module.exports = {
  ...prettierConfig,
  plugins: [...(prettierConfig.plugins || []), 'prettier-plugin-svelte'],
  overrides: [
    ...(prettierConfig.overrides || []),
    {
      files: '*.svelte',
      options: {
        parser: 'svelte',
      },
    },
  ],
};
