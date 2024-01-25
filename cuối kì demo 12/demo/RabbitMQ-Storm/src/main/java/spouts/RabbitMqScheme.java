package spouts;

import lombok.extern.slf4j.Slf4j;
import org.apache.storm.spout.Scheme;
import org.apache.storm.tuple.Fields;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.ArrayList;
import java.util.List;

/**
 * 自定义解析rabbitmq 消息
 * @author wangshuai@e6yun.com
 **/
@Slf4j
public class RabbitMqScheme implements Scheme {


    @Override
    public List<Object> deserialize(ByteBuffer byteBuffer) {
        Charset charset = null;
        CharsetDecoder decoder = null;
        CharBuffer charBuffer = null;
        try {
            charset = Charset.forName("UTF-8");
            decoder = charset.newDecoder();
            charBuffer = decoder.decode(byteBuffer.asReadOnlyBuffer());
            List list = new ArrayList<>(1);
            list.add(charBuffer.toString());
            return list;
        } catch (Exception e) {
            log.error("反序列化公共拓扑消息失败", e);
            return null;
        }
    }

    @Override
    public Fields getOutputFields() {
        return new Fields("message");
    }
}
