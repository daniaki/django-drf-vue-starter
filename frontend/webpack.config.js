const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

// TODO: Create local, staging and product webpack.config.js files

module.exports = {
    
    devtool: 'source-map',
    mode: 'development',
    optimization: {
		    // For debug purposes.
		    minimize: false
	  },
    
    context: __dirname,
    entry: './src/index',
    output: {
        path: path.resolve('./bundles/frontend/'),
        filename: 'app.js'
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
    ],

    module: {
        rules: [
            {
                test: /\.vue$/,
                use: ['ify-loader', 'vue-loader']
            },
            {
                test: /\.js$/,
                use: ['babel-loader'],
                exclude: /node_modules/
            },
            
            {
                test: /\.css$/,
                use: [
                    "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "postcss-loader" // CSS Optimisations
                ]
            },
            {
                test: /\.scss$/,
                use: [
                    "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "sass-loader", // compiles Sass to CSS, using Node Sass by default
                    "postcss-loader" // CSS Optimisations
                ]
            },
            {
                test: /\.(png|jpg|jpeg|gif|eot|ttf|woff|woff2|svg|svgz)(\?.+)?$/,
                use: [{
                    loader: 'url-loader',
                    options: {
                        limit: 100000
                    }
                }]
            }
        ]
    },
    
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js',
            '~': path.resolve(__dirname, 'src')
        },
        extensions: ['.js', '.vue', '.json', '.css', '.scss']
    },
    
    watchOptions: {
        aggregateTimeout: 300,
        poll: 2000
    }
};