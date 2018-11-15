# Practice 最佳实践



1. [The Modular Monolith: Rails Architecture](https://wanqu.co/a/6170/the-modular-monolith-rails-architecture/) : 25个工程师写代码，只有一套 monolithic 的 rails 代码库；搞了两年，5万行代码+10万行测试代码。不搞 microservice，创业初期代码库要做好模块化、依赖关系清晰、边界分明。 
	* Great article! This is a very interesting approach to dealing with a huge rails app — and a nice alternative to micro services. Do you know of any open source projects that use a similar architecture?
	* I think spree uses something similar: https://github.com/spree/spree
	* Have a look at Trailblazer (http://trailblazer.to/). Out of Rails world: Hanami (http://hanamirb.org/)