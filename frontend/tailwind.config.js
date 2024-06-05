/** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: [
//       "./index.html",
//       "./src/**/*.{js,ts,jsx,tsx}",
//       "./node_modules/tw-elements-react/dist/js/**/*.js"
//   ],
//   theme: {
//       extend: {},
//   },
//   darkMode: "class",
//   plugins: [require("tw-elements-react/dist/plugin.cjs")]
//   }

const config = {
content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./src/**/**/**/*.{js,ts,jsx,tsx}",
    "./src/**/*.{js,jsx,ts,tsx}",
    "./src/components/**/*.{js,jsx,ts,tsx}",
    "./src/pages/**/*.{js,jsx,ts,tsx}",
    "./node_modules/tw-elements-react/dist/js/**/*.js"
],
theme: {
    extend: {
        colors: {
            'costom-black-1': '#181818',
            'costom-black-2': '#262626',
            'costom-black-3': '#363636',
            'costom-black-4': '#515151',
        },
    },
},
plugins: [],
darkMode: "class",
//plugins: [require("tw-elements-react/dist/plugin.cjs")]
};

export default config;