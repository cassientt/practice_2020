### BeanShell:
跨线程传递，需要借助beanshell取样器，先将变量通过setProperty函数设置为全局变量，然后其他线程再通过P函数去引用，具体做法如下：
* 1）提取变量：例如通过Json提取器提取到需要使用的参数,并创建参数名:countryId
* 2）使用beanshell设置全局变量：通过beanshell 后置处理程序把提取到的参数设置为全局变量:${__setProperty(AllthreadCountryId,${countryId},true)}       
${countryId}：需要在函数助手中调用__setProperty
特别注意：   
当在函数中设置的全局变量名称与调用时写的变量名称一致时，会出现提取不值的情况
* 3）其它线程组引用变量（变量生效）：用户定义变量countryId = ${__P(AllthreadCountryId,)},在请求中直接调用countryId变量即可。