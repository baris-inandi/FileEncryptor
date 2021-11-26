const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    mode: 'jit',
    purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            fontFamily: {
                'title': ['"Sora"', ...defaultTheme.fontFamily.sans],
            },
            height: {
                'fit-content': 'fit-content'
              },
            width: {
                'fit-content': 'fit-content',
            }
        },
        maxWidth: {
            '1/2': '50%',
            '2/3': '67%'
        }
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
