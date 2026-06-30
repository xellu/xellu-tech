from nautica import Service, Config, ConfigBuilder

class XyzConfig(Service):
    def onInstall(self):
        Config.New("xyz",
            ConfigBuilder()
                .add("contact.webhookUrl", "", comment="Discord webhook URL")
                .build()
        )
        
    def isEnabled(self):
        return True
    
Service.Export(XyzConfig)