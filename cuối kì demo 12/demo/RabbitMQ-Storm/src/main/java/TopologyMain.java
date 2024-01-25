import bolts.OutputBolt;
import bolts.WriterBolt;
import com.rabbitmq.client.ConnectionFactory;
import io.latent.storm.rabbitmq.Declarator;
import io.latent.storm.rabbitmq.RabbitMQSpout;
import io.latent.storm.rabbitmq.config.ConnectionConfig;
import io.latent.storm.rabbitmq.config.ConsumerConfig;
import io.latent.storm.rabbitmq.config.ConsumerConfigBuilder;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.spout.Scheme;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.tuple.Fields;
import spouts.RabbitMqScheme;

import java.io.IOException;

@Slf4j
public class TopologyMain {
    private static String exchange = "exchange_app";
    private static String queue = "queue_app";
    private static String routingKey = "routing_key_app";
    public static final String EXCHANGE_TYPE = "topic";

    @SneakyThrows
    public static void main(String[] args) {
        TopologyBuilder builder = new TopologyBuilder();
        Scheme scheme = new RabbitMqScheme();
        Declarator declarator = (Declarator) channel -> {
            try {
                channel.exchangeDeclare(exchange, EXCHANGE_TYPE, true);
                channel.queueDeclare(queue, true, false, false, null);
                channel.queueBind(queue, exchange, routingKey);
                channel.basicQos(0, 250, false);
            } catch (IOException e) {
                log.error("ERROR: exchange:[{}],queue:[{}],routingKey:[{}],", exchange, queue, routingKey, e);
            }
            log.debug("ERROR: exchange[{}],queue[{}],routingKey[{}]", exchange, queue, routingKey);
        };
        ConnectionConfig connectionConfig = new ConnectionConfig("localhost", 5672, "guest", "guest", ConnectionFactory.DEFAULT_VHOST, 10);
        ConsumerConfig spoutConfig = new ConsumerConfigBuilder().connection(connectionConfig)
                .queue("queue_app")
                .prefetch(200)
                .requeueOnFail()
                .build();
        RabbitMQSpout spout = new RabbitMQSpout(scheme, declarator);
        builder.setSpout("PreOfflineSpout", spout,1).addConfigurations(spoutConfig.asMap()).setMaxSpoutPending(200);
        builder.setBolt("OutputBolt", new OutputBolt(), 4).shuffleGrouping("PreOfflineSpout");
        builder.setBolt("WriterBolt", new WriterBolt(), 8).fieldsGrouping("OutputBolt", new Fields("bookName"));
        Config conf=new Config();
        conf.setDebug(false);
        conf.setNumWorkers(5);
        conf.put(Config.TOPOLOGY_MAX_SPOUT_PENDING, 1);
        StormTopology topology = builder.createTopology();
        LocalCluster cluster = new LocalCluster();
        cluster.submitTopology("HelloStorm", conf,topology );
    }

    private static void RemoteSubmitTopology(TopologyBuilder builder, Config conf) {
        try {
            StormSubmitter.submitTopology("HelloStorm", conf, builder.createTopology());
            Thread.sleep(1000);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
