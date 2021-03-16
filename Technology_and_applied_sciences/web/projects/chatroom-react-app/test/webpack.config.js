const webpack = require('webpack')
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')


module.exports = {
	entry: './src/index.js',
	output: {
    	path: path.resolve(__dirname, "./dist"), // string
    	filename: "bundle.js", // string
    },
    mode: 'development', 
    devServer: {
	    contentBase: path.join(__dirname, 'dist'), 
	    port: 3000,
	    compress: true, // enable gzip compression
	    historyApiFallback: {
	    	index: 'index.html'
	    }, 
	    hot: true, 
	    https: false, // true for self-signed, object for cert authority
	    noInfo: true, // only errors & warns on hot reload
    },

    module:{
    	rules:[
    		{
    			test: /\.jsx?$/,
    			use: {
    				loader: "babel-loader",
    				options: {
    					presets: ['es2015', 'react', 'stage-2'],
    				}
    			}
    		},
            {
                    test: /\.css$/,
                    use:[
                        {
                            loader: 'style-loader',
                        },
                        {
                            loader: 'css-loader',
                        }
                    ]
                },
    	]
    },

    plugins: [
    	new webpack.HotModuleReplacementPlugin(),
    ]
}